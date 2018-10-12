class WordCount:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value'
        buffer = ""
        for c in line:
            if c == " " and buffer:
                yield buffer, 1
                buffer = ""
            elif c != " ":
                buffer += c
        if buffer:
            yield buffer, 1
            buffer = ""

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value'
        count = 0
        for v in values:
            count += 1
        yield key, count
