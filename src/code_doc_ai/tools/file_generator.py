from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os

class FileGeneratorInput(BaseModel):
    """Input schema for FileGenerator."""
    directory: str = Field(..., description="Directory to create file in")
    filename: str = Field(..., description="Name of file to create")
    content: str = Field(..., description="Content to write to file")

class FileGenerator(BaseTool):
    name: str = "File Generator"
    description: str = "Creates markdown files in the specified directory structure"
    args_schema: Type[BaseModel] = FileGeneratorInput

    def _run(self, directory: str, filename: str, content: str) -> str:
        # Set base output directory
        base_dir = "output-report"
        
        # If directory starts with base_dir, don't add it again
        if directory.startswith(base_dir):
            full_directory = directory
        else:
            full_directory = os.path.join(base_dir, directory)
        
        # Ensure directory exists
        os.makedirs(full_directory, exist_ok=True)
        
        # Create full file path
        file_path = os.path.join(full_directory, filename)
        
        # Write content to file
        with open(file_path, 'w') as f:
            f.write(content)
            
        return f"Created file: {file_path}" 