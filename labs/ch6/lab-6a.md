## Understanding the PHONY Directive (Lab 6a)

\subsubsection{Create a Small Makefile}
\justify{}
Create a small two-line Makefile. Be sure to use a tab character to indent the second line.

\begin{mybox}{\thetcbcounter: Small two-line Makefile}
	\lstinputlisting{code/23-makefiles/6a-create}
\end{mybox}

\subsubsection{Test the Makefile}

\justify{}
Test the Makefile by running the ``make'' command. Notice that you can
type ``make'' or ``make code'' and get the same result.

\begin{mybox}{\thetcbcounter: First Test}
	\lstinputlisting{code/23-makefiles/6a-test1}
\end{mybox}

\subsubsection{Test Again with PHONY}

\justify{}
Now edit the Makefile to include the PHONY directive. Be mindful of the
leading dot character.

\begin{mybox}{\thetcbcounter: Add PHONY}
	\lstinputlisting{code/23-makefiles/6a-test2}
\end{mybox}

\justify{}
Try running make again.

\begin{mybox}{\thetcbcounter: Run make}
	\lstinputlisting{code/23-makefiles/6a-test3}
\end{mybox}

\justify{}
Note that the output occurs twice. To suppress the extra output, you can prepend the command with an ampersand character like so:

\begin{mybox}{\thetcbcounter: Suppress extra Output}
	\lstinputlisting{code/23-makefiles/6a-test4}
\end{mybox}

\justify{}
Now try running one final time.

\begin{mybox}{\thetcbcounter: Suppress extra Output}
	\lstinputlisting{code/23-makefiles/6a-test5}
\end{mybox}

\justify{}
Now we get the desired result without the printing of the command
by make.
