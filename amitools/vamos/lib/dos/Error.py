NO_ERROR = 0

ERROR_NO_FREE_STORE               = 103
ERROR_TASK_TABLE_FULL             = 105
ERROR_BAD_TEMPLATE                = 114
ERROR_BAD_NUMBER                  = 115
ERROR_REQUIRED_ARG_MISSING        = 116
ERROR_KEY_NEEDS_ARG               = 117
ERROR_TOO_MANY_ARGS               = 118
ERROR_UNMATCHED_QUOTES            = 119
ERROR_LINE_TOO_LONG               = 120
ERROR_FILE_NOT_OBJECT             = 121
ERROR_INVALID_RESIDENT_LIBRARY    = 122
ERROR_NO_DEFAULT_DIR              = 201
ERROR_OBJECT_IN_USE               = 202
ERROR_OBJECT_EXISTS               = 203
ERROR_DIR_NOT_FOUND               = 204
ERROR_OBJECT_NOT_FOUND            = 205
ERROR_BAD_STREAM_NAME             = 206
ERROR_OBJECT_TOO_LARGE            = 207
ERROR_ACTION_NOT_KNOWN            = 209
ERROR_INVALID_COMPONENT_NAME      = 210
ERROR_INVALID_LOCK                = 211
ERROR_OBJECT_WRONG_TYPE           = 212
ERROR_DISK_NOT_VALIDATED          = 213
ERROR_DISK_WRITE_PROTECTED        = 214
ERROR_RENAME_ACROSS_DEVICES       = 215
ERROR_DIRECTORY_NOT_EMPTY         = 216
ERROR_TOO_MANY_LEVELS             = 217
ERROR_DEVICE_NOT_MOUNTED          = 218
ERROR_SEEK_ERROR                  = 219
ERROR_COMMENT_TOO_BIG             = 220
ERROR_DISK_FULL                   = 221
ERROR_DELETE_PROTECTED            = 222
ERROR_WRITE_PROTECTED             = 223
ERROR_READ_PROTECTED              = 224
ERROR_NOT_A_DOS_DISK              = 225
ERROR_NO_DISK                     = 226
ERROR_NO_MORE_ENTRIES             = 232

ERROR_IS_SOFT_LINK                = 233
ERROR_OBJECT_LINKED               = 234
ERROR_BAD_HUNK                    = 235
ERROR_NOT_IMPLEMENTED             = 236
ERROR_RECORD_NOT_LOCKED           = 240
ERROR_LOCK_COLLISION              = 241
ERROR_LOCK_TIMEOUT                = 242
ERROR_UNLOCK_ERROR                = 243

ERROR_BUFFER_OVERFLOW             = 303     # User or internal buffer overflow
ERROR_BREAK                       = 304     # A break character was received
ERROR_NOT_EXECUTABLE              = 305     # A file has E bit cleared

dos_error_strings = {
NO_ERROR                         :'NO ERROR',

ERROR_NO_FREE_STORE              :'ERROR_NO_FREE_STORE',
ERROR_TASK_TABLE_FULL            :'ERROR_TASK_TABLE_FULL',
ERROR_BAD_TEMPLATE               :'ERROR_BAD_TEMPLATE',
ERROR_BAD_NUMBER                 :'ERROR_BAD_NUMBER',
ERROR_REQUIRED_ARG_MISSING       :'ERROR_REQUIRED_ARG_MISSING',
ERROR_KEY_NEEDS_ARG              :'ERROR_KEY_NEEDS_ARG',
ERROR_TOO_MANY_ARGS              :'ERROR_TOO_MANY_ARGS',
ERROR_UNMATCHED_QUOTES           :'ERROR_UNMATCHED_QUOTES',
ERROR_LINE_TOO_LONG              :'ERROR_LINE_TOO_LONG',
ERROR_FILE_NOT_OBJECT            :'ERROR_FILE_NOT_OBJECT',
ERROR_INVALID_RESIDENT_LIBRARY   :'ERROR_INVALID_RESIDENT_LIBRARY',
ERROR_NO_DEFAULT_DIR             :'ERROR_NO_DEFAULT_DIR',
ERROR_OBJECT_IN_USE              :'ERROR_OBJECT_IN_USE',
ERROR_OBJECT_EXISTS              :'ERROR_OBJECT_EXISTS',
ERROR_DIR_NOT_FOUND              :'ERROR_DIR_NOT_FOUND',
ERROR_OBJECT_NOT_FOUND           :'ERROR_OBJECT_NOT_FOUND',
ERROR_BAD_STREAM_NAME            :'ERROR_BAD_STREAM_NAME',
ERROR_OBJECT_TOO_LARGE           :'ERROR_OBJECT_TOO_LARGE',
ERROR_ACTION_NOT_KNOWN           :'ERROR_ACTION_NOT_KNOWN',
ERROR_INVALID_COMPONENT_NAME     :'ERROR_INVALID_COMPONENT_NAME',
ERROR_INVALID_LOCK               :'ERROR_INVALID_LOCK',
ERROR_OBJECT_WRONG_TYPE          :'ERROR_OBJECT_WRONG_TYPE',
ERROR_DISK_NOT_VALIDATED         :'ERROR_DISK_NOT_VALIDATED',
ERROR_DISK_WRITE_PROTECTED       :'ERROR_DISK_WRITE_PROTECTED',
ERROR_RENAME_ACROSS_DEVICES      :'ERROR_RENAME_ACROSS_DEVICES',
ERROR_DIRECTORY_NOT_EMPTY        :'ERROR_DIRECTORY_NOT_EMPTY',
ERROR_TOO_MANY_LEVELS            :'ERROR_TOO_MANY_LEVELS',
ERROR_DEVICE_NOT_MOUNTED         :'ERROR_DEVICE_NOT_MOUNTED',
ERROR_SEEK_ERROR                 :'ERROR_SEEK_ERROR',
ERROR_COMMENT_TOO_BIG            :'ERROR_COMMENT_TOO_BIG',
ERROR_DISK_FULL                  :'ERROR_DISK_FULL',
ERROR_DELETE_PROTECTED           :'ERROR_DELETE_PROTECTED',
ERROR_WRITE_PROTECTED            :'ERROR_WRITE_PROTECTED',
ERROR_READ_PROTECTED             :'ERROR_READ_PROTECTED',
ERROR_NOT_A_DOS_DISK             :'ERROR_NOT_A_DOS_DISK',
ERROR_NO_DISK                    :'ERROR_NO_DISK',
ERROR_NO_MORE_ENTRIES            :'ERROR_NO_MORE_ENTRIES',
                                 
ERROR_IS_SOFT_LINK               :'ERROR_IS_SOFT_LINK',
ERROR_OBJECT_LINKED              :'ERROR_OBJECT_LINKED',
ERROR_BAD_HUNK                   :'ERROR_BAD_HUNK',
ERROR_NOT_IMPLEMENTED            :'ERROR_NOT_IMPLEMENTED',
ERROR_RECORD_NOT_LOCKED          :'ERROR_RECORD_NOT_LOCKED',
ERROR_LOCK_COLLISION             :'ERROR_LOCK_COLLISION',
ERROR_LOCK_TIMEOUT               :'ERROR_LOCK_TIMEOUT',
ERROR_UNLOCK_ERROR               :'ERROR_UNLOCK_ERROR',
                                 
ERROR_BUFFER_OVERFLOW            :'ERROR_BUFFER_OVERFLOW',
ERROR_BREAK                      :'ERROR_BREAK',
ERROR_NOT_EXECUTABLE             :'ERROR_NOT_EXECUTABLE'
}
