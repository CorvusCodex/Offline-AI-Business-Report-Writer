from utils import run_llama

def business_report(data):
    prompt = f"Write a structured executive summary report based on this data:\n{data}"
    return run_llama(prompt)

if __name__ == "__main__":
    data = open("data.txt").read()
    print(business_report(data))
