# Calculator incident pilot

This workflow establishes the application's existing pytest baseline on an isolated `roost/incident-pilot/**` branch. It also checks pull requests containing the workflow. It does not deploy the application or merge changes.

The initial local baseline is 115 passing tests. The workflow runs the same suite and retains a JUnit report. A dependency-install failure may have no report; use the failing job's log to distinguish setup problems from application defects.

For a controlled incident experiment, enroll the exact workflow and pilot branch in Roost Product Hub. Record the passing baseline run, then introduce one reversible arithmetic defect on that branch. Keep the existing assertions intact. Verify that the next run fails for the intended behavior, that Roost identifies the affected run and source, and that an eligible repair passes the original suite. A proposed PR remains separate from CI recovery and live application recovery.

Do not introduce the defect on the default branch. Retain the original failure, investigation, repair revision and recovery run as distinct evidence. Stop monitoring the pilot when the experiment ends.
