class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 1:
            return [strs]

        substr_map = {}
        sorted_by_alpha_arr = []
        result_ls = []
        for string in strs:
            sorted_by_alpha_arr.append("".join(sorted(string)))

        print(sorted_by_alpha_arr)
        for i in range(len(sorted_by_alpha_arr)):
            if sorted_by_alpha_arr[i] not in substr_map:
                substr_map[sorted_by_alpha_arr[i]] = [strs[i]] 
            elif sorted_by_alpha_arr[i] in substr_map:
                substr_map[sorted_by_alpha_arr[i]].append(strs[i])

        for k,v in enumerate(substr_map.values()):
            result_ls.append(v)
        
        return result_ls

        