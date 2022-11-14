def quickSort(nums):
  def _quickSort(nums, start, end):
    if start >= end:
      return

    x = nums[start:end][len(nums[start:end]) // 2]

    l = start 
    r = end

    while l <= r:

      while nums[l] < x:
        l += 1

      while nums[r] > x:
        r -= 1

      if l <= r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
      
    _quickSort(nums, start, r)
    _quickSort(nums, l, end)
      
    
  _quickSort(nums, 0, len(nums) - 1)


def combSort(nums):
  length = int(len(nums) / 1.247)
  swap = 1
  while length > 1 or swap > 0:
    swap = 0
    i = 0
    while i + length < len(nums):
      if nums[i] > nums[i+length]:
        nums[i], nums[i+length] = nums[i+length], nums[i]
        swap += 1
      i += 1
    if length > 1:
      length = int(length / 1.247)

  

