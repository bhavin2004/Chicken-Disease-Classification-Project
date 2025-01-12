
import sys


def get_error_details(error_name:Exception,error_detail:sys)->str:
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    
    error_msg = f"There is error in python script {file_name} at line no: {exc_tb.tb_lineno}\n And Error=> {error_name}"
    
    return error_msg


class CustomException(Exception):
    def __init__(self,error_name:Exception,error_detail:sys)->None:
        super().__init__(error_name)
        self.error_msg = get_error_details(error_name,error_detail)
        
    def __str__(self):
        return self.error_msg
    
    
    
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        raise CustomException(e,sys)