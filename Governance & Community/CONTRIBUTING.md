# Contributing to NER-Aegis AI

Thank you for your interest in improving landslide risk intelligence for Northeast India! 

## 🎯 Project Scope

NER-Aegis AI is a **prototype** decision-support system for disaster management authorities. Contributions should maintain:
- ✅ Focus on decision support (not prediction)
- ✅ Explainability and transparency
- ✅ Human-in-the-loop design
- ✅ Conservative, safety-first approach

## 🚀 How to Contribute

### Reporting Issues
- Check existing issues first
- Provide clear description and steps to reproduce
- Include system information (OS, Python version)

### Suggesting Enhancements
- Explain the problem it solves
- Consider deployment context (NE India)
- Align with safety-critical design principles

### Code Contributions

**Before coding:**
1. Open an issue to discuss the change
2. Ensure it aligns with project goals
3. Check for existing work

**Development setup:**
```bash
# Clone repository
git clone https://github.com/your-org/ner-aegis-ai.git
cd ner-aegis-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest

# Run application
streamlit run app.py
```

**Code standards:**
- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include type hints where appropriate
- Test your changes thoroughly
- Keep logic separate from UI (`logic/` folder)

**Commit messages:**
```
feat: Add confidence interval display
fix: Correct evacuation priority calculation
docs: Update installation instructions
style: Format code with black
```

### Pull Request Process

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
6. **Push to your fork**
7. **Open a Pull Request**

**PR checklist:**
- [ ] Code follows project style
- [ ] Docstrings added/updated
- [ ] README updated if needed
- [ ] No breaking changes (or documented)
- [ ] Tested locally

## 🛡️ Safety-Critical Guidelines

This system deals with **life-safety decisions**. All contributions must:

1. **Never overstate capabilities** - No claims of prediction accuracy
2. **Maintain conservative thresholds** - Better false alarm than missed warning
3. **Preserve explainability** - Users must understand WHY
4. **Keep humans in control** - AI advises, humans decide
5. **Document limitations** - Be honest about failure modes

## 📋 Priority Areas

We especially welcome contributions in:

- 🧪 **Validation**: Testing with historical landslide data
- 🌐 **Localization**: Additional language support
- 📊 **Visualization**: Improved data presentation
- 🔧 **Performance**: Optimization for low-bandwidth areas
- 📚 **Documentation**: User guides, API docs

## ❌ What We Don't Accept

- Claims of prediction accuracy
- Features that remove human oversight
- Complexity that reduces explainability
- Changes that ignore safety considerations
- Undocumented algorithms

## 🤝 Code of Conduct

- Be respectful and professional
- Focus on the issue, not the person
- Welcome diverse perspectives
- Assume good faith
- Remember: lives may depend on this system

## 📞 Questions?

- Open an issue with the `question` label
- Check existing documentation first
- Be specific about your use case

## 🙏 Thank You

Every contribution helps improve disaster preparedness in Northeast India. Your work could save lives.

---

**Remember:** This is a prototype for demonstration. Real deployment requires institutional partnerships, multi-year validation, and authority approval.
