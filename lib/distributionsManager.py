from lib.utilities import get_truncated_normal


class DistributionsManager:

    def __init__(self, yaml_parser):
        self.number_of_subjects_distribution = self.build_number_of_subjects_distribution(yaml_parser)

    @staticmethod
    def build_number_of_subjects_distribution(yaml_parser):
        distribution_type = yaml_parser.number_of_subjects_per_user_distribution
        if distribution_type == "normal" or distribution_type is None:
            if yaml_parser.number_of_subjects_per_user_mean is None:
                mean = 4.8
            else:
                mean = yaml_parser.number_of_subjects_per_user_mean
            if yaml_parser.number_of_subjects_per_user_sd is None:
                sd = 1.2
            else:
                sd = yaml_parser.number_of_subjects_per_user_sd
            if yaml_parser.number_of_subjects_per_user_lower_bound is None:
                lower_bound = 1
            else:
                lower_bound = yaml_parser.number_of_subjects_per_user_lower_bound
            if yaml_parser.number_of_subjects_per_user_upper_bound is None:
                upper_bound = 7
            else:
                upper_bound = yaml_parser.number_of_subjects_per_user_upper_bound
            return get_truncated_normal(mean=mean, sd=sd, lower_bound=lower_bound, upper_bound=upper_bound)
