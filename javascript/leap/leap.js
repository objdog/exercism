function isLeap(year) {
    if(year % 2 === 0) {
        if(year % 100 === 0) {
            if(year % 400 === 0){
                return true
            }
            return false
        }return true
    }return false
}

