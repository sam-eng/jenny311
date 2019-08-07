# Samantha Eng

import watson_developer_cloud

# Set up Assistant service.
service = watson_developer_cloud.AssistantV2(
	version = '2018-09-20',
    username= 'apikey',
    password = '[insert api key here]' #replace with API Key
)

assistant_id = '4cde2101-84d4-460b-bbb1-bac49e5ce061' # replace with assistant ID

# Create session.
session_id = service.create_session(
    assistant_id = assistant_id
).get_result()['session_id']

user_input = ''
print("To leave the conversation with Jenny311, say 'bye' !")
while user_input != 'bye':
	response = service.message(
		assistant_id,
		session_id,
		input = {
			'text': user_input
		}
	).get_result()

	print(response['output']['generic'][0]['text'])

	user_input = input('>> ')
print("Thanks for chatting with Jenny311!")
# We're done, so we delete the session.
service.delete_session(
    assistant_id = assistant_id,
    session_id = session_id
)
