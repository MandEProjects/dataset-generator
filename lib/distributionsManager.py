from lib.utilities import get_truncated_normal, get_truncated_exponential


class DistributionsManager:

    def __init__(self, yaml_parser):
        self.favorite_subjects_per_user_distribution = self.build_favorite_subjects_distribution(yaml_parser)
        self.subjects_distribution = self.build_subjects_distribution(yaml_parser)
        self.age_distribution = self.build_age_distribution(yaml_parser)

    @staticmethod
    def build_favorite_subjects_distribution(yaml_parser):
        distribution_type = yaml_parser.favorite_subjects_per_user_distribution
        if distribution_type == "normal" or distribution_type is None:
            if yaml_parser.favorite_subjects_per_user_mean is None:
                mean = 4.8
            else:
                mean = yaml_parser.favorite_subjects_per_user_mean
            if yaml_parser.favorite_subjects_per_user_sd is None:
                sd = 1.2
            else:
                sd = yaml_parser.favorite_subjects_per_user_sd
            if yaml_parser.favorite_subjects_per_user_lower_bound is None:
                lower_bound = 1
            else:
                lower_bound = yaml_parser.favorite_subjects_per_user_lower_bound
            if yaml_parser.favorite_subjects_per_user_upper_bound is None:
                upper_bound = 7
            else:
                upper_bound = yaml_parser.favorite_subjects_per_user_upper_bound
            return get_truncated_normal(mean=mean, sd=sd, lower_bound=lower_bound, upper_bound=upper_bound)
        if distribution_type == "exponential":
            if yaml_parser.favorite_subjects_scale is None:
                scale = 2
            else:
                scale = yaml_parser.favorite_subjects_scale
            if yaml_parser.favorite_subjects_per_user_lower_bound is None:
                lower_bound = 1
            else:
                lower_bound = yaml_parser.favorite_subjects_per_user_lower_bound
            if yaml_parser.favorite_subjects_per_user_upper_bound is None:
                upper_bound = 10
            else:
                upper_bound = yaml_parser.favorite_subjects_per_user_upper_bound
            return get_truncated_exponential(upper_bound, lower_bound, scale)

    @staticmethod
    def build_subjects_distribution(yaml_parser):
        distribution_type = yaml_parser.subjects_distribution
        if distribution_type == "exponential" or distribution_type is None:
            if yaml_parser.subjects_scale is None:
                scale = 2
            else:
                scale = yaml_parser.subjects_scale
            if yaml_parser.subjects_lower_bound is None:
                lower_bound = 1
            else:
                lower_bound = yaml_parser.subjects_lower_bound
            if yaml_parser.subjects_upper_bound is None:
                upper_bound = 10
            else:
                upper_bound = yaml_parser.subjects_upper_bound
            return get_truncated_exponential(upper_bound, lower_bound, scale)
        if distribution_type == "normal":
            if yaml_parser.subjects_mean is None:
                mean = 4.8
            else:
                mean = yaml_parser.subjects_mean
            if yaml_parser.subjects_sd is None:
                sd = 1.2
            else:
                sd = yaml_parser.subjects_sd
            if yaml_parser.subjects_lower_bound is None:
                lower_bound = 1
            else:
                lower_bound = yaml_parser.subjects_lower_bound
            if yaml_parser.subjects_upper_bound is None:
                upper_bound = 7
            else:
                upper_bound = yaml_parser.subjects_upper_bound
            return get_truncated_normal(mean, sd, lower_bound, upper_bound)

    @staticmethod
    def build_age_distribution(yaml_parser):
        if yaml_parser.age_mean is None:
            mean = 37
        else:
            mean = yaml_parser.age_mean
        if yaml_parser.age_sd is None:
            sd = 6
        else:
            sd = yaml_parser.age_sd
        if yaml_parser.age_lower_bound is None:
            lower_bound = 20
        else:
            lower_bound = yaml_parser.age_lower_bound
        if yaml_parser.age_upper_bound is None:
            upper_bound = 60
        else:
            upper_bound = yaml_parser.age_upper_bound
        return get_truncated_normal(mean, sd, lower_bound, upper_bound)