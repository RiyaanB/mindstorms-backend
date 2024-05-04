from openai import OpenAI
import uuid

# openai.api_key = 'sk-proj-OUOET3Yuu7uvB59kqDR5T3BlbkFJThoqZuiS29RO9EEvx7ep'
client = OpenAI(api_key='sk-proj-OUOET3Yuu7uvB59kqDR5T3BlbkFJThoqZuiS29RO9EEvx7ep')

class Hive:
    def __init__(self, objective):
        self.users = []
        self.tasks = {}
        self.global_context = f"GLOBAL CONTEXT:\n {objective}"
        self.generate_new_tasks_from_context([])

    def get_unassigned_task(self):
        for id, task in self.tasks.items():
            if task['status'] == 'unassigned':
                task['status'] = "pending"
                return task
        return None

    def interact_with_gpt4(self, prompt):
        # Send the prompt to GPT-4
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{'role': 'user', 'content': prompt}]
        )

        return response.choices[0].message.content

    def register_user(self, user_data):
        # Add user to the system
        self.users[user_data['username']] = user_data['profile_summary']

    def generate_tasks(self):
        # Logic to generate and assign tasks based on the global context and user profiles
        pass

    def get_system_status(self):
        # Return current status of the system
        return {
            "users": len(self.users),
            "active_tasks": len([t for t in self.tasks.values() if t['status'] == 'active']),
            "completed_tasks": len([t for t in self.tasks.values() if t['status'] == 'completed']),
        }
    
    def generate_new_tasks_from_context(self, pending_tasks):
        prompt = self.global_context
        prompt += "\nPending tasks:\n"
        print(pending_tasks)
        if len(pending_tasks) > 5:
            return
        for task in pending_tasks:
            prompt += f"\n{task['description']}"
        prompt += "\nBased on the above, give a newline-separated list of 5 tasks which are needed to move towards the objective"
        response =  self.interact_with_gpt4(prompt)
        task_descriptions = str(response).split('\n')
        for description in task_descriptions:
            self.tasks[uuid.uuid4()].append({
                'description': description,
                'status': 'unsassigned',
            })

    def update_gc_with_task_result(self, task):
        prompt = self.global_context
        prompt += f"\n We just finished this task: '{task['description']}' and the result was '{task['result']}'\n Rewrite the above global context with the task response:"
        self.global_context = self.interact_with_gpt4(prompt)