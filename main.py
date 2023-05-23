from resources import load_document, creating_model, question_answering
import sys


def main():
    print("Welcome to your personal OpenAI powered Chatbot\n")
    print("\n")
    print("--------------------------------------------\n")
    print("\n")
    print("\n")
    print("\n")
    print("Please choose one of the options")
    app_input = int(input("1) Create Agent\n2) Exit\n\n"))
    if app_input == 1:
        print("\n\n\nHi, I am your personal agent.\n I will help you in answering all your query.\n\n\n")
        print("\n\nBut first please provide a path to document and document name\n\n")
        print("\n\nPlease upload the file in pdf format\n\n")
        path = input("path to document:  \n\n")
        name = input("Document name: \n\n")
        docs = load_document(path,name)
        model = creating_model(docs)
        try:
            while True:
                input_query = input("\n\nPlease Ask your queries\n\npress crtl+c to exit the program\n\n")
                answer = question_answering(model, input_query)
                print(answer['result'])
        except KeyboardInterrupt:
            print("Exiting program now")
            sys.exit(0)
            
        
    elif app_input ==2:
        sys.exit(0)


main()
    