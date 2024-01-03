from joblib import load

label_encoder = {
    'normal weight Low health risk':0,
    'over weight Low health risk':1,
    'Obesity Low health risk':2,
    'Obesity High health risk':3,
    'under weight Low health risk':4 
}

back_to_label = {v:k for k,v in label_encoder.items()}
back_to_label

model = load('model\\final_model.joblib')

def prediction(age,w,h,a):
    wthr = a/h
    bmi = calculate_bmi(w,h)
    input = [[age,w,h,a,wthr,bmi]]
    prediction = model.predict(input)
    return back_to_label[prediction.item()]

def calculate_bmi(weight,height):
    return weight / (height ** 2)

if __name__ == "__main__":
    age = int(input("enter the age"))
    w = float(input("enter the weight"))
    h = float(input("enter the height"))
    a = float(input("enter the abdomen"))

    print(prediction(age,w,h,a))