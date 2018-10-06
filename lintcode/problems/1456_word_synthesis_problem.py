class Solution:
    """
    @param target: the target string
    @param words: words array
    @return: whether the target can be matched or not
    """

    def matchFunction(self, target, words):
        # Write your code here

        # build mapping for bipartite
        # each char from target is left
        # each word from words is right
        connection = self.build_connection(target, words)
        matched = {}
        max_match = 0

        # from each left char, search argumentign path
        for cidx, c in enumerate(target):
            node = ("char", cidx)
            if node in matched:
                continue
            visited = set()
            visited.add(node)
            if self.found_aug_path(node, connection, visited, matched):
                max_match += 1
                if max_match == len(target):
                    return True
        return max_match == len(target)

    def found_aug_path(self, node, connection, visited, matched):
        type, idx = node
        for cnt in connection[node]:
            if cnt in visited:
                continue
            visited.add(cnt)
            if cnt not in matched or self.found_aug_path(
                matched[cnt], connection, visited, matched
            ):
                matched[cnt] = node
                matched[node] = cnt
                return True
        return False

    def build_connection(self, target, words):
        connection = collections.defaultdict(set)
        for cidx, c in enumerate(target):
            for widx, w in enumerate(words):
                if c in w:
                    connection["char", cidx].add(("word", widx))
                    connection["word", widx].add(("char", cidx))
        return connection


"""
matched need to store the counterpart, because in L37 you are searching the counter part's matched
To understand how the path is a 交替路, pay attention to L37
Here, either node => cnt has cnt unmatched to anyone, here it is an augmenting path found
Or, if cnt is already matched to some other (which is garanteed not node), then we say, let's see
if we can find an augmenting path from the guy that cnt is currently matching to. If there is a path,
then our node can steal cnt 
"""
