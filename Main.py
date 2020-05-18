
def max_cal(ar, l, h):
		left_sum=-1000000
		sm=0
		mid = (h+l)//2
		for i in range(mid, l-1,-1):
			sm=sm+ar[i]
			if(sm>left_sum):
				left_sum=sm

		right_sum=-1000000
		sm=0

		for i in range(mid+1,h+1):
			sm=sm+ar[i]
			if(sm>right_sum):
				right_sum=sm

		return left_sum+right_sum

def max_sum(arr, l, h):

		if(h==l):
			return arr[h]
		mid = (h+l)//2

		max_left=max_sum(arr, l, mid)
		max_right=max_sum(arr, mid+1,h)
		max_c=max_cal(arr, l, h)

		return max(max_left,max_right,max_c)

A = [1,2,3,5,3,45,21,342,1]
sol = max_sum(A, 0, len(A)-1)
print(sol)
#update test pull and push
