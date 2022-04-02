import xlrd  # pip install xlrd

startFromWhichRow = 1   # in case the first row has no rules but only column titles put 1 otherwise 0
sheetNumber = 0  # the index of the excel sheet you want to process, if doOnlyOneSheet is False it will do them all starting from this index
doOnlyOneSheet = False  # if for any reason you need to do one file at a time put this to True (capital T)
serviceTaskID = "SCTASK1234567"  # number of the Jira Service Task that is inserted in the line of the comments
redirectType = "301"  # can be 301 or 302, your choice
rewriteRulesFlags = ["NC", "L", "R="+redirectType, "ENV=REDIRECTCACHE:1"]  # add all the redirect flags you need

pathFileToRead = 'W:\\Example\\Local\\Folder\\myExcelFileWithRules.xlsx'    # path of the file to read
excel_file_path = xlrd.open_workbook(pathFileToRead)
excel_sheet = excel_file_path.sheet_by_index(sheetNumber)

# example of a RewriteRule with a comment on the line before
# # SCTASK1234567 --- https://www.test.co.uk/en/some/old/path.html => https://www.test.co.uk/en/a/new/path.html
# RewriteRule ^/en/some/old/path.html$ https://%{SERVER_NAME}/en/a/new/path.html? [NC,L,R=301,ENV=REDIRECTCACHE:1]

commentBeforeRewriteRule = "# " + serviceTaskID + " --- "
rewriteRule = "RewriteRule ^/"

pathFileToWrite = open("W:\\Example\\Local\\Folder\\rewrited-rules.txt", "w")  # path of the file to write to
pathFileToWrite.write("#################### SHEET NUMBER " + str(sheetNumber+1) + " - "
           + excel_file_path.sheet_by_index(sheetNumber).name
           + " #################### \n\n")

# creating the string with redirect flags that we will attach to the RedirectRules below
flagsToString = "["
for i in range(len(rewriteRulesFlags)):
    if rewriteRulesFlags[i] != rewriteRulesFlags[-1]:
        flagsToString += rewriteRulesFlags[i] + ","
    else:
        flagsToString += rewriteRulesFlags[i] + "]"

for worksheets in excel_file_path.sheet_names():
    excel_sheet = excel_file_path.sheet_by_index(sheetNumber)

    for row in range(startFromWhichRow, excel_sheet.nrows):
        rewriteRule = "RewriteRule ^/"
        commentBeforeRewriteRule = "# " + serviceTaskID + " --- "

        # row/column of the old URL
        urlFrom = excel_sheet.cell_value(row, 0)
        urlFromSplitted = urlFrom.split("/")

        # row/column of the new
        urlTo = excel_sheet.cell_value(row, 1)
        urlToSplitted = urlTo.split("/")

        # It is the comment of the line before the rewrite rule with the number of Service Task (if needed)
        commentBeforeRewriteRule += excel_sheet.cell_value(row, 0) + " => " + excel_sheet.cell_value(row, 1)

        # create the first URL of the RewriteRule
        for i in range(3, len(urlFromSplitted)):
            if i != len(urlFromSplitted)-1:
                rewriteRule += urlFromSplitted[i] + "/"
            else:
                rewriteRule += urlFromSplitted[i] + "$ "

        rewriteRule += "https://%{SERVER_NAME}/"

        # create the second URL of the RewriteRule
        for i in range(3, len(urlToSplitted)):
            if i != len(urlToSplitted)-1:
                rewriteRule += urlToSplitted[i] + "/"
            else:
                rewriteRule += urlToSplitted[i] + "? " + flagsToString

        pathFileToWrite.write(commentBeforeRewriteRule + "\n")
        pathFileToWrite.write(rewriteRule + "\n\n")

    # if you want to do only one sheet at a time interrupts the "for" here
    if doOnlyOneSheet:
        break

    # otherwise, increments the index by the page number and moves to the next sheet until the end of the file
    if sheetNumber < len(excel_file_path.sheet_names())-1:
        sheetNumber += 1
        pathFileToWrite.write("\n\n #################### SHEET NUMBER " + str(sheetNumber+1) + " - "
                   + excel_file_path.sheet_by_index(sheetNumber).name
                   + " #################### \n\n")

pathFileToWrite.close()
