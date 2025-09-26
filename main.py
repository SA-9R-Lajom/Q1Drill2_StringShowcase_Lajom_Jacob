@when("click, #submit-btn")
def show_message(event):
   
    name_input = document.getElementById("name-input")
    age = document.getElementById("age-input").value
    school = document.getElementById("school-input").value

    message = f"Hello, {name_input.value}! You are {age} years old and attend {school}."
    alert(message) name_input = document.getElementById("name-input")

    document.querySelector ("#output").innerText= "" 

    message = f"Hello, {name_input.value}! You are {age} years old and attend {school}."
    Name : (name)
    Age  : (age)
    School : (school)


display(message, target="#output")
