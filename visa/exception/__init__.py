import os 
import sys
 
class CustomException(Exception):
    def __init__(self, error_message:Exception , error_detail: sys):
        self.error_message = CustomException.get_detailed_error_message(error_message = error_message, 
                                                                        error_detail=error_detail)
        
    def get_detailed_error_message( error_message:Exception,error_detail:sys )->str:
        _,_,exec_tb = error_detail.exc_info()
        exception_block_line_number=exec_tb.tb_frame.f_lineno
        try_block_line_number=exec_tb.tb_lineno
        file_name=exec_tb.tb_frame.f_code.co_filename   ## calling the main project file name(visa ) and Inside file name ing calling here
        error_message= f""" 
        Error occured in our script :
        [{file_name }] at
        try block line number at :[{try_block_line_number}] and execption_block_line_number at : [{exception_block_line_number}]
        error message: [{error_message}]
        """
        return error_message                

    def __str__(self):
        return self.error_message
    
    def __repr__(self) -> str:
        return CustomException.__name__.str()



    

