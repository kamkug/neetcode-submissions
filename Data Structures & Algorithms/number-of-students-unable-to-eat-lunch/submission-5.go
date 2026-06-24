func countStudents(students []int, sandwiches []int) int {
    var zero, one int
    for _, s := range students {
        switch s {
            case 0:
                zero++
            case 1:
                one++
        }
    }


    for _, s := range sandwiches {
        switch s {
            case 0:
                if zero == 0 {
                    goto End
                }
                zero--
            case 1:
                if one == 0 {
                    goto End
                }
                one--
        }
    }
    End:

    return zero+one
}