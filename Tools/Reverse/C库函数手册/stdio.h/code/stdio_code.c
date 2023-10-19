#include <stdio.h>
#include <stdlib.h>

//-----------------------------------------------------------------//
// stdio.h -> FILE *fopen(const char *filename, const char *mode); //
//-----------------------------------------------------------------//
int main_fopen(void)
{
	FILE* fp = fopen("file.txt","r"); //file content: Hello world!
	if(!fp)
	{
		perror("File opening faild");
		return EXIT_FAILURE;
	}
	
	int c; //note:int, not char, required to handle EOF
	while((c = fgetc(fp)) != EOF) //standard C I/O file reading loop
	{
		putchar(c);
	}
	
	if(ferror(fp))
		puts("\nI/O error when reading\n");
	else if(feof(fp))
		puts("\nEnd of file reached successfully\n");

	fclose(fp);

    getchar(); //for console pause
    return 0;
}

//---------------------------------------------------------------------------------//
// stdio.h -> FILE *freopen(const char *filename, const char *mode, FILE* stream); //
//---------------------------------------------------------------------------------//
int main_freopen(void)
{
    puts("stdout is printed to console");
    if (freopen("file_reopen.txt", "w", stdout) == NULL)
    {
       perror("freopen() failed");
       return EXIT_FAILURE;
    }
    puts("stdout is redirected to a file"); // this is written to file_reopen.txt
    fclose(stdout);
    
    getchar(); //for console pause
    return 0;
}

//-----------------------------------------//
// stdio.h -> int fclose(FILE * stream); //
//-----------------------------------------//
int main_close(void)
{
    FILE* fp = fopen("file.txt", "r"); //file content:Hello world!
    if(!fp) {
        perror("File opening failed");
        return EXIT_FAILURE;
    }
 
    int c; // note: int, not char, required to handle EOF
    while ((c = fgetc(fp)) != EOF)  // standard C I/O file reading loop
    {
       putchar(c);
    }
 
    if (ferror(fp))
        puts("\nI/O error when reading\n");
    else if (feof(fp))
        puts("\nEnd of file reached successfully\n");
 
    fclose(fp);
    
    getchar(); //for console pause
    return 0;
}

//-----------------------------------------------//
// stdio.h -> int remove(const char * filename); //
//-----------------------------------------------//
int main_remove(void)
{
    FILE* fp = fopen("file_remove.txt", "w"); // create file
    if(!fp) { perror("file_remove.txt"); return 1; }
    puts("Created file_remove.txt");
    fclose(fp);
 
    int rc = remove("file_remove.txt"); 
    if(rc) { perror("remove"); return 1; }
    puts("Removed file_remove.txt");
 
    fp = fopen("file_remove.txt", "r"); // Failure: file does not exist
    if(!fp) perror("Opening removed file failed");
 
    rc = remove("file_remove.txt"); // Failure: file does not exist
    if(rc) perror("Double-remove failed");
    
    getchar(); //for console pause
    return 0;
}

//----------------------------------------------------------------------------//
// stdio.h -> int rename(const char *old_filename, const char *new_filename); //
//----------------------------------------------------------------------------//
int main_rename(void)
{
    FILE* fp = fopen("file_name.txt", "w"); // create file "file_name.txt"
    if(!fp) { perror("file_name.txt"); return 1; }
    fputc('a', fp); // write to "file_name.txt"
    fclose(fp);
 
    int rc = rename("file_name.txt", "file_rename.txt");
    if(rc) { perror("rename"); return 1; }
 
    fp = fopen("file_rename.txt", "r");
    if(!fp) { perror("file_rename.txt"); return 1; }
    printf("%c\n", fgetc(fp)); // read from "to.txt"
    fclose(fp);
    
    getchar(); //for console pause
    return 0;
}


int main(void)
{


	getchar(); //for console pause
    return 0;
}
