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
        if len(
            friend_name_split := friend_name.split(".")
        ) > 1:
            if friend_name_split[0].lower() in {"mr", "mrs", "ms", "miss"}:
                return f"Hello, {friend_name}!"
            raise ValueError("Invalid input: friend_name cannot be empty")
        return f"Hello, World!"

