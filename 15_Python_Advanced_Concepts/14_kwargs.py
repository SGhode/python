def marks(**kwargs):
    # kwargs is a dictionary that captures all keyword arguments passed to the function
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(Shivam=90, Anshika=95, Shubham=85, Rishabh=80, Shivraj=98)