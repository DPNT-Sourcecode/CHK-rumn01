class HelloSolution:

    # friend_name = unicode string
    def hello(self, friend_name):
        if not isinstance(friend_name, str):
            raise ValueError("Invalid input: friend_name must be a string")
        try:
            friend_name.encode("utf-8").decode("utf-8")
        except UnicodeError:
            raise ValueError(
                "Invalid input: friend_name must be a valid unicode string"
            )
        return f"Hello, {friend_name}!"
