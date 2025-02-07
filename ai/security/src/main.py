from ai.security.src.crew import SecurityBase


class RunTestCrew(SecurityBase):

    def run(self, topic: str):
        inputs = {'topic': topic}
        self.crew().kickoff(inputs=inputs)


a = RunTestCrew()
a.run('API_KEY=1231')
