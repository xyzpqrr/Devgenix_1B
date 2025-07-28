import subprocess

def summarize_with_ollama(prompt, model="phi:2"):
    """
    Uses the lightweight phi:2 model from Ollama for local summarization.
    Returns a summary generated from the given prompt.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", model, "-p", prompt],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "[SUMMARY ERROR: TIMEOUT]"
    except Exception as e:
        return f"[SUMMARY ERROR: {str(e)}]"

def build_prompt(section, persona, job):
    """
    Builds a focused summarization prompt using persona and job-to-be-done context.
    """
    return f"""You are helping a {persona} whose task is: {job}

Here is a relevant section from a document:

Title: {section['title']}
Page: {section['page']}

Content:
{section['content']}

Give a concise, relevant summary (3-5 sentences) focused on what helps accomplish the task.
"""
