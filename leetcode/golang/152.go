// https://leetcode.com/problems/maximum-product-subarray/
/**
The solution entails computing the product in both directions.
Since 0 refreshes all product to itself (i.e. 0), reset to a unit product(i.e. 1)
Get the maximum product from both direction, and return as result
*/

func maxProduct(nums []int) int {
    if len(nums) == 1 {
        return nums[0]
    }

    N := len(nums)
    maxProd := -11
    forward, backward := 1, 1

    for i := range len(nums) {
        if forward == 0 {
            forward = 1
        }
        if backward == 0 {
            backward = 1
        }

        forward *= nums[i]
        backward *= nums[N-i-1]
        maxProd = max(maxProd, max(forward, backward))
    }
    return maxProd
}
