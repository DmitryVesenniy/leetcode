func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    numsAll := mergeSlices(nums1, nums2)

	if len(numsAll)%2 == 0 {
		meanIndex := int(len(numsAll)/2) - 1
		return float64(numsAll[meanIndex]+numsAll[meanIndex+1]) / 2
	}
	meanIndex := int(len(numsAll) / 2)
	return float64(numsAll[meanIndex])
}

func mergeSlices(nums1 []int, nums2 []int) []int {
	if len(nums1) == 0 {
		return nums2
	}
	if len(nums2) == 0 {
		return nums1
	}

	start_index1 := nums1[0]
	start_index2 := nums2[0]

	var firstNums []int
	var lastNums []int

	if start_index1 <= start_index2 {
		firstNums = nums1
		lastNums = nums2
	} else {
		firstNums = nums2
		lastNums = nums1
	}
	numsAll := make([]int, 0, len(nums1)+len(nums2))
	index := 0
	for _, v := range firstNums {
		if index < len(lastNums) && v > lastNums[index] {
			for _, value := range lastNums[index:] {
				if v > value {
					numsAll = append(numsAll, value)
					index++
				} else {
					break
				}
			}
		}
		numsAll = append(numsAll, v)
	}

	numsAll = append(numsAll, lastNums[index:]...)

	return numsAll
}