package golang
// https://leetcode.com/problems/product-of-array-except-self/
/**
The solution must be computed without using the division operation.

For each position, compute the prefix product of all the elements in the array except itself.
In the reverse order, compute the postfix product of the prefix and the input array element.

Time: O(N)
Space: O(1), where the output array does not count
*/

func productExceptSelf(nums []int) []int {
    N := len(nums)
	if N == 2 {
        return []int{nums[1], nums[0]}
    }

    ans := make([]int, N)
    
	// prefix product
	ans[0] = 1
    for i := 1; i < N; i++ {
        ans[i] = nums[i-1] * ans[i-1]
    }

	// postfix produxt
	post := 1
    for i := N - 1; i > 0; i-- {
        ans[i] = post * ans[i]
		post *= nums[i]
    }

    return ans
}
