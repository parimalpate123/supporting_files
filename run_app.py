from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/current/nlu')
agent = Agent.load('./models/current/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-525465834114-524864270065-563460979138-dad624215e4093532da3dac9f1860b50', #app verification token
							'xoxb-525465834114-525382855891-Iu7vDtYbPUvqfDcaXck54bbc', # bot verification token
							'N7oZdLwzfCZ3sm1syUsTn0Nl', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
