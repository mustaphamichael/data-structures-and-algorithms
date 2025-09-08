package golang

// https://leetcode.com/problems/logger-rate-limiter/

type Logger struct {
    Next map[string]int
    Interval int
}


func Constructor() Logger {
    return Logger{Next: make(map[string]int), Interval: 10}
}


func (this *Logger) ShouldPrintMessage(timestamp int, message string) bool {
    if next, ok := this.Next[message]; ok {
        if next <= timestamp {
            this.Next[message] = timestamp + this.Interval
            return true
        }
        return false
    }

    this.Next[message] = timestamp + this.Interval
    return true
}


/**
 * Your Logger object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.ShouldPrintMessage(timestamp,message);
 */
