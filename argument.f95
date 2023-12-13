program main
    implicit none
    character(len=*), parameter :: VERSION = '1.0'
    character(len=32)           :: arg
    integer                     :: i

    do i = 1, command_argument_count()
        call get_command_argument(i, arg)

        select case (arg)
            case ('-v', '--version')
                print '(2a)', 'version ', VERSION
                stop

            case ('-h', '--help')
                call print_help()
                stop

            case ('-t','--t')
                print '(2a, /)', 'unrecognised command-line option: ', arg
                call data_type()
                stop
               case default
                print '(2a, /)', 'unrecognised command-line option: ', arg
                call print_help()
                stop  
        end select
    end do
contains
    subroutine print_help()
        print '(a, /)', 'command-line options:'
        print '(a)',    '  -v, --version     print version information and exit'
        print '(a, /)', '  -h, --help        print usage information and exit'
    end subroutine print_help
   subroutine data_type()
       print '(a,/)','command-line statement:'
       print*,1+2
   end subroutine
 end program main
