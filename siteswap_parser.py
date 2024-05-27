import re

class Siteswap:
    def __init__(self, sequence):
        self.sequence = sequence
        self.num_balls = None
        self.period = None
        self.is_valid = False
        self.error = None
        self.sequence_details = []
        self._validate_and_parse()

    def _validate_and_parse(self):
        try:
            # Normalize character set
            full_code = self.sequence.upper()

            # Check for multiplex or synchronous patterns
            if re.match(r'^[0-9A-Z]+$', full_code):
                self._parse_vanilla(full_code)
            elif re.match(r'^([0-9A-Z]*(\[[1-9A-Z]{2,}\])+[0-9A-Z]*)+$', full_code):
                self._parse_multiplex(full_code)
            elif re.match(r'^(\([02468ACEGIKMOQSUWY]X?,[02468ACEGIKMOQSUWY]X?\))+\*?$', full_code):
                self._parse_synchronous(full_code)
            elif re.match(r'^(\(([02468ACEGIKMOQSUWYX]X?|\[[2468ACEGIKMOQSUWYX]{2,}\]),([02468ACEGIKMOQSUWY]X?|\[[2468ACEGIKMOQSUWY]{2,}\])\))+\*?$', full_code):
                self._parse_synchronous_multiplex(full_code)
            else:
                self.error = "Invalid syntax"
                return

            # Check the number of balls and period
            self.num_balls = int(sum(self.sequence_details) / len(self.sequence_details))
            self.period = len(self.sequence_details)

            # Check if the sequence is valid by ensuring every beat has balanced throws
            self.is_valid = self._check_balance()
        except Exception as e:
            self.error = str(e)

    def _parse_vanilla(self, full_code):
        self.sequence_details = [int(c, 36) for c in full_code]

    def _parse_multiplex(self, full_code):
        self.sequence_details = []
        for char in full_code:
            if char.isalnum():
                self.sequence_details.append(int(char, 36))
            elif char == '[':
                continue
            elif char == ']':
                continue
            else:
                raise ValueError("Invalid multiplex character")

    def _parse_synchronous(self, full_code):
        self.sequence_details = []
        synch_pairs = re.findall(r'\((.*?)\)', full_code)
        for pair in synch_pairs:
            left, right = pair.split(',')
            left_value = int(left.replace('X', ''), 36)
            right_value = int(right.replace('X', ''), 36)
            self.sequence_details.extend([left_value, right_value])

    def _parse_synchronous_multiplex(self, full_code):
        self.sequence_details = []
        synch_pairs = re.findall(r'\((.*?)\)', full_code)
        for pair in synch_pairs:
            left, right = pair.split(',')
            left_value = sum(int(c.replace('X', ''), 36) for c in left if c.isalnum())
            right_value = sum(int(c.replace('X', ''), 36) for c in right if c.isalnum())
            self.sequence_details.extend([left_value, right_value])

    def _check_balance(self):
        total_throws = sum(self.sequence_details)
        return total_throws % len(self.sequence_details) == 0

    def get_info(self):
        if not self.is_valid:
            return {"isValid": self.is_valid, "error": self.error}
        print({
            "isValid": self.is_valid,
            "siteswap": self.sequence,
            "numBalls": self.num_balls,
            "period": self.period,
            "sequence": self.sequence_details
        })
        return {
            "isValid": self.is_valid,
            "siteswap": self.sequence,
            "numBalls": self.num_balls,
            "period": self.period,
            "sequence": self.sequence_details
        }

# Example usage
# if __name__ == "__main__":
#     siteswap1 = "333"
#     ss1 = Siteswap(siteswap1)
#     print(ss1.get_info())
