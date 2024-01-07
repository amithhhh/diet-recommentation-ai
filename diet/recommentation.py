from joblib import load


back_to_label = {
    0: 'Normal Weight and healthy',
    1: 'Overweight ',
    2: 'Obesity Class I ',
    3: 'Obesity Class III',
    4: 'Obesity Class II ',
    5: 'slender'

}

model = load('dt1.joblib')

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