class Solution:
	def replace_value(self,arr,k):
		"""传入一个代替换的值，若存在，则进行替换，否则不做替换"""
		try:
			idx = arr.index(k)
			arr[idx] = 0
		except ValueError:
			print('不做替换')
		return arr

if __name__ == "__main__":
	solution = Solution()
	t = solution.replace_value([1,2,3,4,5],9)
	print(t)