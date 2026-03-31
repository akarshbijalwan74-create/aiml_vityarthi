from src.auth import login
from src.model import get_trained_model, predict_category
from src.logger import log_action

def main():
    if not login():
        return

    print("Initializing AI Model...")
    model = get_trained_model()
    log_action("System Started. Model Trained.")

    while True:
        ticket = input("Enter support ticket text (or 'exit'): ")
        if ticket.lower() == 'exit':
            break
        
        prediction = predict_category(model, ticket)
        print(f"--> AI Classification: [ {prediction} ]\n")
        log_action(f"Classified '{ticket}' as {prediction}")

if __name__ == "__main__":
    main()
