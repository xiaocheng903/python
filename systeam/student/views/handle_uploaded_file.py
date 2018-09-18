
class handle_uploaded_file:
    def handle_uploaded_file(f):
        with open('../name.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)