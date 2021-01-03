class phone:
    def call(self):
        print("call")
    def message(self):
        print("message")

class samsung(phone):
    def photo(self):
        print("photo")


sam = samsung()
sam.call()
sam.message()
sam.photo()
print(issubclass(samsung,phone))