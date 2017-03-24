import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    prompt = """
    Select the operation you want to perform [1-5]
    :
    1. Average
    2. Max
    3. Min
    4. Sum
    5. Exit
    """

    while True:
        # get user input
        response = raw_input(prompt)
        if response in set(["1", "2", "3", "4"]):
            # parse the corresponding operation text
            operation = {1: "avg", 2: "max", 3: "min", 4: "sum"}[int(response)]

            # retrieve data
            c.execute("SELECT {}(nums) FROM nums".format(operation))

            get = c.fetchone()

            print operation + ": %f" % get[0]

        elif response == "5":
            print "Exit"
            break
