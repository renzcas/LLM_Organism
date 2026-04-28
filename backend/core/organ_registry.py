from organs.opcode_knowledge import opcode_knowledge_router

def register_organs(app):
    app.include_router(opcode_knowledge_router)
