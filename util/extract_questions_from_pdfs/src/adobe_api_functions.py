import logging
import os.path

from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_renditions_element_type import ExtractRenditionsElementType

class AdobeApiFunctions:
    async def extract_info_from_pdf(path_in, path_out):
        try:
            # get base path.
            base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

            # Initial setup, create credentials instance.
            credentials = Credentials.service_account_credentials_builder() \
                .from_file(base_path + "/extract_questions_from_pdfs/credentials/pdfservices-api-credentials.json") \
                .build()

            # Create an ExecutionContext using credentials and create a new operation instance.
            execution_context = ExecutionContext.create(credentials)
            extract_pdf_operation = ExtractPDFOperation.create_new()

            # Set operation input from a source file.
            source = FileRef.create_from_local_file(f"{base_path}/extract_questions_from_pdfs/{path_in}")
            extract_pdf_operation.set_input(source)

            # Build ExtractPDF options and set them into the operation
            extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
                .with_elements_to_extract([ExtractElementType.TEXT]) \
                .with_elements_to_extract_renditions([ExtractRenditionsElementType.FIGURES]) \
                .with_get_char_info(True) \
                .build()
            extract_pdf_operation.set_options(extract_pdf_options)

            # Execute the operation.
            result: FileRef = extract_pdf_operation.execute(execution_context)

            # Save the result to the specified location.
            result.save_as(f"{base_path}/extract_questions_from_pdfs/{path_out}")
        except (ServiceApiException, ServiceUsageException, SdkException):
            logging.exception("Exception encountered while executing operation")
            
        
        
        
