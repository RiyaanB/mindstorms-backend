from openai import OpenAI

# openai.api_key = 'sk-proj-OUOET3Yuu7uvB59kqDR5T3BlbkFJThoqZuiS29RO9EEvx7ep'
client = OpenAI(api_key='sk-proj-OUOET3Yuu7uvB59kqDR5T3BlbkFJThoqZuiS29RO9EEvx7ep')

class Hive:
    def __init__(self):
        self.users = {}
        self.tasks = {}
        self.global_context = ""

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
        # TODO: User will input the prompt for generating new tasks here
        # For now, this is a placeholder for the actual implementation
        prompt = self.global_context
        prompt += "\nPending tasks:\n"
        print(pending_tasks)
        for task in pending_tasks:
            prompt += f"\n{task['description']}"
        prompt += "\nBased on the above, give a newline-separated list of 5 tasks which are needed to move towards the objective"
        response =  self.interact_with_gpt4(prompt)
        return str(response).split('\n')
    
    def update_gc_with_task_result(self, task):
        prompt = self.global_context
    

tasks = [{'description': 'testing'}]
print(Hive().generate_new_tasks_from_context(tasks))