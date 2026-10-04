#!/usr/bin/env python3
"""Compatibility entry point for the sales-led static site builder."""
from build_sales_site import main
from build_blog_shell import main as build_blog_shell
from build_workflow_visual import main as build_workflow_visual

if __name__ == "__main__":
    build_workflow_visual()
    main()
    build_blog_shell()
