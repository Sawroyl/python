interested=input('Enter intrested field')
expect = int(input('Enter expected salary'))
while True:

    if expect>20000:
        exp=int(input('Enter years of experience:'))
        if exp>=2:
            print('you are shortlisted your enquiry has been recorded, we will notify you, thank you!!')
        else:
            print('your enquiry has been recorded, we will notify you, thank you!!')

    else:
        print('your enquiry has been recorded, we will notify you, thank you!!')
    break