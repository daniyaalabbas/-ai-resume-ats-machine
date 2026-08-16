import re


def extract_keywords(text):
    """
    Extract useful technical/professional keywords from text.
    """

    text = text.lower()

    # Common technical terms we want to recognize
    known_keywords = [
        "azure",
        "aws",
        "gcp",
        "linux",
        "windows",
        "kubernetes",
        "docker",
        "openshift",
        "terraform",
        "ansible",
        "jenkins",
        "github actions",
        "gitlab",
        "argocd",
        "helm",
        "python",
        "bash",
        "shell scripting",
        "networking",
        "tcp/ip",
        "dns",
        "ssh",
        "firewall",
        "nginx",
        "apache",
        "ci/cd",
        "devops",
        "cloud",
        "monitoring",
        "prometheus",
        "grafana",
        "rbac",
        "iam",
        "vnet",
        "subnet",
        "load balancer",
        "virtual machine",
        "storage",
        "sql",
        "rest api",
        "git",
    ]

    found = []

    for keyword in known_keywords:
        if keyword in text:
            found.append(keyword)

    return sorted(set(found))


def calculate_ats_score(resume, job_description):

    resume_keywords = set(extract_keywords(resume))
    jd_keywords = set(extract_keywords(job_description))

    if not jd_keywords:
        return {
            "score": 0,
            "matched": [],
            "missing": [],
        }

    matched = sorted(resume_keywords & jd_keywords)
    missing = sorted(jd_keywords - resume_keywords)

    score = round((len(matched) / len(jd_keywords)) * 100)

    return {
        "score": score,
        "matched": matched,
        "missing": missing,
    }
