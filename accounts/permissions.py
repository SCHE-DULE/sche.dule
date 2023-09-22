PERMISSIONS_MAP = {
            "RECEPTIONIST": [
                "add_client",
                "schedule_appointment",
                "set_client_payment",
                "view_scheduled_appointments",
            ],
            "THERAPIST": [
                "view_scheduled_appointments",
                "close_own_schedule",
                "view_own_contract",
            ],
            "MANAGER": [
                "manage_receptionists",
                "modify_patient_information",
            ],
            "GENERAL_MANAGER": [
                "approve_new_tasks",
                "manage_accounting",
                "manage_suppliers",
            ],
            "ADMINISTRATOR": [
                "modify_all_roles",
                "manage_therapists",
                "delegate_tasks",
                "review_all_functions",
            ],
            "SUPER_USER": [
                "manage_custom_functionality",
                "adapt_system_to_needs",
            ],
        }