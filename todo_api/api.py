from flask import Flask
from flask_restful import Resource, Api,abort,reqparse

app = Flask(__name__)
api = Api(app)


# class hello(Resource):
#     def get(self):
#         return {'data':'hello world'}
    
# class helloname(Resource):
#     def get(self,name):
#         return {'data' : 'Hello, {}'.format(name)}
    
# api.add_resource(hello,'/helloworld')
# api.add_resource(helloname,'/name/<string:name>')  
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task",type=str,help="Task is required.",required=True)
task_post_args.add_argument("Summary",type=str,help="Summary is required.",required=True)

todos = {1:{'task':'hellow world program',"summary":"write the code using python"},
         2:{'task':'task2',"summary":"writing code task 3"},
         3:{'task':'task3',"summary":"writing code task 3"}
         }
class ToDoList(Resource):
    def get(self):
        return todos
      
class ToDo(Resource):
    def get(self,todo_id):
        return todos[todo_id]  
    
    def post(self,todo_id):
        args = task_post_args.parse_args()
        if todo_id in todos:
            abort(409,"Task is already taken")
        todos[todo_id] =  {"task":args["task"],"summary":args["summary"]}
    
    
api.add_resource(ToDoList,'/todo')
api.add_resource(ToDo,'/todos/<int:todo_id>')     

if __name__ == "__main__":
    app.run(debug=True)