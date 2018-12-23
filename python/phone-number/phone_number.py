class Phone(object):
    def __init__(self, phone_number):
        self.number = self.format_phone_number(phone_number)
        self.area_code = self.format_phone_number(phone_number)[0:3]
        self.exchange_code = self.format_phone_number(phone_number)[3:6]
        self.subscriber_number = self.format_phone_number(phone_number)[6:10]

        if self.area_code[0] == "0" or self.area_code[0] == "1":
            raise ValueError("Please input a valid area code")
        elif self.exchange_code[0] == "0" or self.exchange_code[0] == "1":
            raise ValueError("Please input a valid exchange code")


    def format_phone_number(self, number):
        number = ''.join(c for c in number if c.isdigit())
        if len(number) < 10 or len(number) > 11:
            raise ValueError("Please input a valid phone number")
        if len(number) == 10:
            return number
        elif len(number) != 10 and number[0] == "1":
            return number[-10:]
        else:
            raise ValueError("Please input a valid phone number")


    def pretty(self):
        return "(%s) %s-%s" % (self.area_code, self.exchange_code, self.subscriber_number)