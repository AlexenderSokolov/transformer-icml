# Diagnostic scope and run record

The script computes each finite binomial tail as a Python exact rational; it then converts the tail to binary float for the logged value and comparison with the floating exp bound. Very small tails can underflow to 0.0, so the logged decimal is not an exact rational rendering, and these checks do not independently prove the analytic inequality. M, k, theta, row, p, mu, and the strict threshold are logged exactly. Cases with k>0 occur at M=1024, 4096, and 16384. All 60 combinations passed.

Before the completed run, an initial shell wrapper had a mismatched quotation mark in the intended redirection. Bash reported a nonexistent output path and did not start the Python program or create the diagnostic log. The second command used shell noclobber and created the log once. The note and script were created before that first attempted run. No random data, random initialization, or prior research files were modified.
