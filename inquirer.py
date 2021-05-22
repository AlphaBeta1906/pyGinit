from prompt_toolkit.validation import Validator, ValidationError

class validator(Validator):
	def validate(self,document):
		print(document.text)
		if document.text == None:
			raise ValidationError(message="Please dont leave an empty value",
                                  cursor_position=len(document.text))
		else:
			pass


file = open("gitignore-list.txt","r")
arr = []
for text in file:
	arr.append(text.replace('.gitignore' , ' '))


questions = [
    {
		'type' : "input",
		"name" : "repo_name",
		"message":"Enter the name for your repo : ",
		 "validate": validator,
	},
	{
		'type': "input",
		"name" : "description",
		"message" :"Enter description of your repo (leave blank if you dont have one) : ",
		"validate": validator,
	},
    {
    	'type' : "list",
    	"name" : "repo_type",
    	"message":"select your github repo type",
    	'choices': ["public","private"],
    	"validate": validator,
    },

    {
    	'type' : "list",
    	"name" : "gitginore_template",
    	"message" : "Select gitginore template for your repo",
    	'choices' : arr,
    	"validate": validator,
    },
    {
    	'type' : "confirm",
    	"name" : "readme_confirm",
    	"message" : "Do you want to create readme for your repo ? ",
    	"validate": validator,
    },
]


