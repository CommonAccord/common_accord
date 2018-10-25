Model.Root={H} {W}{!}

=[B]

B.=[B]

H={B.C.B.C.B.C.H}

!=, and how!


Good=Does extreme recursive cross referencing with no problem.  These are rarely used, but an easy error to make.

Bug1=A reference to a non-existent file (map) throws an error, even if the map is not used in rendering.  I.e., the expansion is not fully lazy.  This may not be a problem in our experimentation, but in production the exhaustic expansion will create performance problems, and maybe worse (circular references).

Bug2=If there is no match for a key named foo, then return  {foo} in the output text.



